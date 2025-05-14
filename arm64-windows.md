```sh
set VCPKG_INSTALL_OPTIONS=--allow-unsupported
```

```sh
vcpkg install --triplet arm64-windows --allow-unsupported
```


      C:\Users\thoma\Source\valhalla\vcpkg\buildtrees\luajit\install-arm64-windows-rel-out.log
      C:\Users\thoma\Source\valhalla\vcpkg\buildtrees\luajit\install-arm64-windows-rel-err.log


```sh
cmake -B build -DCMAKE_TOOLCHAIN_FILE=%CD%\vcpkg\scripts\buildsystems\vcpkg.cmake -DENABLE_SERVICES=OFF -DVCPKG_TARGET_TRIPLET=arm64-windows -DVCPKG_OVERLAY_PORTS=%CD%\overlay-ports-vcpkg  -DVCPKG_INSTALL_OPTIONS="--allow-unsupported" -DCMAKE_BUILD_TYPE=Release
```
