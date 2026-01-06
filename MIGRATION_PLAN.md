# Supabase Migration Plan - Version 2.0

## Overview
Migrating from YAML file storage to Supabase for data persistence, and implementing admin-only features.

## Key Features to Implement

### 1. Supabase Integration
- [ ] Set up Supabase project and database
- [ ] Create database schema for events
- [ ] Create database schema for user/admin authentication
- [ ] Replace YAML file loading with Supabase queries
- [ ] Replace localStorage with Supabase as primary data source
- [ ] Implement real-time updates (optional)

### 2. Admin Mode
- [ ] Implement authentication system (Supabase Auth)
- [ ] Create admin login page
- [ ] Add admin check middleware/guards
- [ ] Restrict profile image editing to admin only
- [ ] Restrict event management (add/edit/delete) to admin only
- [ ] Add admin indicator in UI when logged in
- [ ] Implement logout functionality

### 3. Database Schema

#### Events Table
```sql
- id (uuid, primary key)
- date (date)
- name (text)
- desc (text, nullable)
- category (text, nullable)
- tags (text[], nullable)
- link (text, nullable)
- images (text[], nullable)
- created_at (timestamp)
- updated_at (timestamp)
```

#### Admin/Users Table (Supabase Auth)
- Use Supabase built-in authentication
- Create admin role/permission system

### 4. Migration Steps
1. Set up Supabase project
2. Create database tables
3. Migrate existing YAML data to Supabase
4. Update frontend to use Supabase client
5. Implement authentication flow
6. Add admin guards to protected routes/actions
7. Test and deploy

## Files to Modify
- `index.html` - Add Supabase client, auth checks, admin guards
- `events.html` - Add Supabase client, admin-only access
- Create `admin.html` or add admin login to existing pages
- Remove/replace YAML file loading logic
- Update data persistence layer

## Environment Variables Needed
- `VITE_SUPABASE_URL` or `SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY` or `SUPABASE_ANON_KEY`

## Notes
- Keep backward compatibility during migration if possible
- Consider data export/import functionality
- Plan for zero-downtime migration

