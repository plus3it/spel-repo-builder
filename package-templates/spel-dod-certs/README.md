# spel-dod-certs

Provides a package to install and update DoD CA certificates.

# How to Update DoD_CAs.pem

DISA periodically releases a new DoD CA bundle. These bundles are published here:

* <https://public.cyber.mil/pki-pke/>

Notifications of updates to the bundle go out via the "Tools" RSS feed:

* <https://public.cyber.mil/pki-pke/rss-2/>

When a new bundle is published, follow these instructions to update `spel-dod-certs`:

1. Download the new bundle and extract it
2. Identify the `*pem.p7b` file in the bundle
3. Run this command to export the CA certificates to a concatenated PEM file:
    ```
    openssl pkcs7 -in *pem.p7b -print_certs -out DoD_CAs.pem
    ```
4. Create a new branch in this project
5. Replace the `DoD_CAs.pem` file with the new version
6. Update `spel-dod-certs.spec` with the new version and a changelog entry
7. Commit the change and open a pull request
