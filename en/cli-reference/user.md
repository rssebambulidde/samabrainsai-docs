# User

## List User Emails

This command allows you to list all user emails registered in the system.

### Local Usage

```bash
pnpm user
```

Or if using npm

```bash
npx samaflow user
```

### Docker Usage

If you're running SamaFlow in a Docker container, use the following command:

```bash
docker exec -it FLOWISE_CONTAINER_NAME pnpm user
```

Replace `FLOWISE_CONTAINER_NAME` with your actual SamaFlow container name.

## Reset User Password

This command allows you to reset a user's password.

### Local Usage

```bash
pnpm user --email "admin@admin.com" --password "myPassword1!"
```

Or if using npm

```
npx samaflow user --email "admin@admin.com" --password "myPassword1!"
```

### Docker Usage

If you're running SamaFlow in a Docker container, use the following command:

```bash
docker exec -it FLOWISE_CONTAINER_NAME pnpm user --email "admin@admin.com" --password "myPassword1!"
```

Replace `FLOWISE_CONTAINER_NAME` with your actual SamaFlow container name.

### Parameters

* `--email`: The email address of the user whose password you want to reset
* `--password`: The new password to set for the user
