-- 添加superuser
INSERT INTO auth_user (
  password,
  is_superuser, username, email, first_name, last_name, is_staff, is_active, date_joined
) VALUES (
  "pbkdf2_sha256$150000$p9sZVXszd6je$VhV3fyMmsh3uAsjOqcKBxNhZ9cGkQQS3bFsdc+jjANs=",
  1, "admin", "a@qq.com", "", "", 1, 1, 'now'
);

-- 用户数据
INSERT INTO u_account(id, name, active, status, created_time) VALUES (1, 'User1', 1, 1, 'now');
INSERT INTO u_account(id, name, active, status, created_time) VALUES (2, 'User2', 1, 1, 'now');

-- 权限数据
INSERT INTO u_permission(id, created_time, updated_time, code, description, long_description, parent_permission_id)
  VALUES (1, 'now', 'now', 'perms.users', 'Users', 'Users permission', '');

INSERT INTO u_permission(id, created_time, updated_time, code, description, long_description, parent_permission_id)
  VALUES (2, 'now', 'now', 'perms.users.view', 'View user', 'View user permission', '1');

INSERT INTO u_permission(id, created_time, updated_time, code, description, long_description, parent_permission_id)
  VALUES (3, 'now', 'now', 'perms.users.create', 'Create user', 'Create user permission', '1');

INSERT INTO u_permission(id, created_time, updated_time, code, description, long_description, parent_permission_id)
  VALUES (4, 'now', 'now', 'perms.users.edit', 'Edit user', 'Edit user permission', '1');

-- 角色数据
INSERT INTO u_role(id, title, created_time) VALUES (1, 'Admin', 'now');
INSERT INTO u_role(id, title, created_time) VALUES (2, 'User', 'now');

-- 角色权限
INSERT INTO u_role_permissions(role_id, permission_id) VALUES (1, 1);
INSERT INTO u_role_permissions(role_id, permission_id) VALUES (1, 2);
INSERT INTO u_role_permissions(role_id, permission_id) VALUES (1, 3);
INSERT INTO u_role_permissions(role_id, permission_id) VALUES (1, 4);

-- 用户角色
INSERT INTO u_account_role(account_id, role_id, created_time) VALUES (1, 1, 'now');
INSERT INTO u_account_role(account_id, role_id, created_time) VALUES (2, 2, 'now');
