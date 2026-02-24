import os
import re
import shutil

ROOT = r'e:\OXYBIO'
CSS_FILE = os.path.join(ROOT, 'assets', 'css', 'styles.css')

# ─── Read CSS ──────────────────────────────────────────────────
with open(CSS_FILE, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix double semicolons
n = len(re.findall(r';\s*;', css))
css = re.sub(r';\s*;', ';', css)
print(f'[CSS] Fixed {n} double-semicolons')

# 2. Remove animation-play-state: paused
if 'animation-play-state: paused;' in css:
    css = css.replace('animation-play-state: paused;', '/* removed: animation-play-state paused */')
    print('[CSS] Removed paused animation state')

# 3. Eliminate the redundant .structure-section 3rem block
old_rule = '    .structure-section { padding-top: 3rem; padding-bottom: 3rem; }'
if old_rule in css:
    css = css.replace(old_rule, '    /* structure-section padding consolidated below */')
    print('[CSS] Removed duplicate .structure-section 3rem override')

# 4. Ensure final definitive block exists (hero clearance authority)
if 'DEFINITIVE MOBILE OVERRIDES' not in css:
    definitive = (
        '\n/* =====================================================\n'
        '   DEFINITIVE MOBILE OVERRIDES\n'
        '   This block has final authority - do not add more below\n'
        '   ===================================================== */\n'
        '@media (max-width: 768px) {\n'
        '    section.structure-section[style*="padding-top"] {\n'
        '        padding-top: 100px !important;\n'
        '    }\n'
        '    .display, h1.display {\n'
        '        font-size: clamp(1.8rem, 9vw, 2.8rem) !important;\n'
        '        line-height: 1.05 !important;\n'
        '        word-break: break-word !important;\n'
        '    }\n'
        '    body { overflow-x: hidden !important; }\n'
        '    img { max-width: 100% !important; height: auto !important; }\n'
        '}\n'
    )
    css += definitive
    print('[CSS] Added definitive mobile overrides block')
else:
    print('[CSS] Definitive mobile block already present')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(css)
print('[CSS] Saved styles.css')

# ─── HTML audit and cache bust ──────────────────────────────────
HTML_PAGES = [
    'index.html', 'about.html', 'science.html', 'ingredients.html',
    'problem.html', 'blog.html', 'careers.html', 'contact.html',
    'terms.html', 'privacy.html',
    'blog-origin.html', 'blog-minerals.html', 'blog-bootstrapping.html'
]

print('\n[HTML] Processing pages...')
for page in HTML_PAGES:
    path = os.path.join(ROOT, page)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove empty style attributes
    before = len(re.findall(r' style=""', html))
    html = html.replace(' style=""', '')

    # Bump cache version to 30
    html = re.sub(r'\?v=\d+"', '?v=30"', html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  [OK] {page} (removed {before} empty styles, cache v30)')

# ─── Move old build/fix scripts to _archive_scripts ─────────────
ARCHIVE_DIR = os.path.join(ROOT, '_archive_scripts')
os.makedirs(ARCHIVE_DIR, exist_ok=True)

SCRIPTS_TO_ARCHIVE = [
    'bust_css_cache.py', 'bust_css_cache_v3.py', 'bust_css_cache_v4.py',
    'bust_css_cache_v5.py', 'bust_css_cache_v6.py', 'bust_css_cache_v7.py',
    'bust_css_cache_v8.py', 'bust_css_cache_v9.py', 'bust_css_cache_v10.py',
    'bust_css_cache_v11.py', 'bust_css_cache_v12.py', 'bust_css_cache_v16.py',
    'bust_global_cache_v15.py', 'bust_global_cache_v23.py',
    'bust_v2_cache.py', 'bust_v3_cache.py', 'bust_v4_cache.py',
    'fluid_hero_clearance.py', 'fix_semicolons_typography.py',
    'fix_overlaps_and_clipping.py', 'enforce_mobile_wrappers.py',
    'fix_rogue_css.py', 'fix_ux_final.py',
    'fix_blank_space.py', 'fix_spacing.py', 'fix_mojibake.py',
    'fix_responsive_spacing.py', 'convert_static_margins.py',
    'fix_about_animations.py', 'fix_about_css.py',
    'fix_careers_hero.py', 'fix_careers_mobile.py', 'fix_final_gaps.py',
    'fix_blog_typography.py', 'fix_links.py', 'fix_readability.py',
    'kill_white_space.py', 'check_overflow.py',
    'build_blog.py', 'build_blog_page.py', 'build_bespoke_1.py', 'build_bespoke_2.py',
    'build_global_ui_perf.py', 'build_index_ui_perf.py', 'build_ingredients_ui_perf.py',
    'build_problem_ui_perf.py', 'add_counter_animation.py', 'append_css.py',
    'apply_justification.py',
    'v2_parallax_inject.py', 'v2_scroll_inject.py', 'v2_text_reveal.py',
    'inject_v2.py', 'inject_magnetic_buttons.py', 'inject_duel_section.py',
    'propagate_v2.py', 'update_colors.py', 'update_css.py', 'update_fonts.py',
    'update_css_blueprint.py', 'update_css_typo.py', 'update_footer.py',
    'update_nav.py', 'update_science_nav.py', 'update_legal_nav.py',
    'update_blog_nav.py', 'update_blog_index.py', 'update_subpages.py',
    'sync_about_nav.py', 'sync_all_mega_menus.py',
    'remove_core_values.py', 'remove_duplicate_table.py',
    'premium_css.py',
    'refine_mega_menu.py', 'refine_mega_menu_v2.py',
    'standardize_hero_spacing.py',
    'unify_badges.py', 'upgrade_animations.py',
    'feat_fix_html_logos.py',
    'fix_mobile_layout.py', 'fix_mobile_ux.py',
    'fix_table_scroll.py', 'fix_grid_padding.py',
    'apply_static_corrections.py', 'audit_fixes.py', 'audit_links.py',
    'fix_apple_scroll.py', 'fix_apple_scroll_layout.py',
    'fix_all_about_issues.py', 'fix_who_section.py', 'fix_who_we_are_tabs.py',
    'fix_science_section.py',
    'premium_hero_and_table.py', 'premium_index_upgrades.py',
    'premium_ingredients_light.py', 'premium_ingredients_light_v2.py',
    'premium_contact_script.py', 'premium_approach_grid.py',
    'premium_about_story.py', 'premium_about_story_light.py',
    'premium_premium_careers.py', 'premium_job_card.py',
    'premium_who_redesign.py',
    'feat_html_edits.py', 'feat_interactive_about.py', 'feat_mobile_ui.py',
    'rebuild_index_structure.py',
    'refactor_about_tabs.py', 'refactor_blog_layout.py',
    'build_apple_scroll.py', 'build_apple_scroll_v2.py',
    'rewrite_apple_scroll_native.py',
    'build_careers.py', 'build_careers_page.py',
    'build_contact.py', 'build_contact_page.py',
    'build_index.py', 'build_ingredients.py',
    'build_legal_pages.py', 'build_privacy.py',
    'build_problem.py',
    'build_science_pages.py', 'build_about.py',
    'premium_careers.py', 'premium_careers_hero.py',
    'fix_smart_tabs.py', 'fix_smart_tabs_sidebar.py',
    'fix_smart_tabs_sidebar_v2.py', 'fix_smart_tabs_sidebar_v3.py',
    'fix_premium_careers_flow.py',
    'convert_careers_tabs.py',
    'create_blog_posts.py',
    'inject_duel_section.py',
    'premium_ingredients_problem.py',
    'bust_v4_cache.py',
    'fix_rogue_css.py',
    'fix_ux_final.py',
]

archived = 0
for script in SCRIPTS_TO_ARCHIVE:
    src = os.path.join(ROOT, script)
    dst = os.path.join(ARCHIVE_DIR, script)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.move(src, dst)
        archived += 1

print(f'\n[CLEANUP] Archived {archived} old scripts to _archive_scripts/')
print('\n[DONE] All audits and fixes applied. Cache version: v30')
