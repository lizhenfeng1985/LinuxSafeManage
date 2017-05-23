#!/bin/bash

DST_DIR=./SafeManage
DST_SERVICE=SafeManageService
DST_UI=SafeManageUI
DST_PKG=SafeManage

# Service
mkdir -p $DST_DIR
mkdir -p $DST_DIR/db
mkdir -p $DST_DIR/license
mkdir -p $DST_DIR/log

# compile
cd Service
/usr/local/go/bin/go build
cd ..

cp Service/db/*.db                 $DST_DIR/db/
cp Service/license/pub.key $DST_DIR/license/pub.key
cp Service/server.key      $DST_DIR/server.key
cp Service/server.crt      $DST_DIR/server.crt
mv Service/Service         $DST_DIR/$DST_SERVICE


# ui

# compile
cp -r UI /tmp/UI
chown -R lzf /tmp/UI
su lzf <<EOF
cd /tmp/UI;
pyinstaller -F -w gui.py
exit;
EOF

cp /tmp/UI/dist/gui   $DST_DIR/$DST_UI 
cp -r UI/static       $DST_DIR/
cp -r UI/html         $DST_DIR/
cp -r UI/config.ini   $DST_DIR/config.ini

tar -zcf $DST_PKG.tar.gz $DST_DIR

# clean dir
rm -rf /tmp/UI 



