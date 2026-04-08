
# Auto-push all changes to GitHub
$repoPath = $PSScriptRoot

git -C $repoPath config user.email "manisreethaar@gmail.com"
git -C $repoPath config user.name "Manisreethaar"

git -C $repoPath add -A

$status = git -C $repoPath status --porcelain
if ($status) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    git -C $repoPath commit -m "chore: website update $timestamp"
    git -C $repoPath push origin main
    Write-Host "`n✅ All changes pushed to GitHub successfully!" -ForegroundColor Green
} else {
    Write-Host "`nℹ️  Nothing to push — working tree is already clean." -ForegroundColor Cyan
}

Read-Host "`nPress Enter to close"
