-- Fix: add missing DELETE policy on formulations (RLS was blocking all deletes silently)
-- Rules: any authenticated user can delete Draft/Archived; only admins can delete Approved.
CREATE POLICY "formulations_delete"
ON public.formulations
FOR DELETE
TO authenticated
USING (
  (status <> 'Approved') OR is_admin()
);
