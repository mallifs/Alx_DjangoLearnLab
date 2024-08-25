first alx django project
# Django Book Management Application

## Permissions Setup

### Custom Permissions

- **can_edit**: Allows users to edit existing books.
- **can_create**: Allows users to create new books.

### User Groups

- **Editors**: Assigned the `can_edit` permission.
- **Creators**: Assigned the `can_create` permission.
- **Viewers**: No special permissions; can only view books.

### Testing Permissions

1. Create users and assign them to the appropriate groups:
   - Editors: Can edit books.
   - Creators: Can create books.
   - Viewers: Can only view books.
2. Log in as these users to verify that permissions are enforced correctly.

### Notes

- Permissions are enforced using Django's `@permission_required` decorator for function-based views and `PermissionRequiredMixin` for class-based views.
- Ensure `raise_exception=True` is used to raise exceptions when users lack the necessary permissions.