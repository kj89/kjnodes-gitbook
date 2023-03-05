# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (42)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,1edd1232fe59fd00a13bfdd9ac273e48b20f11c3@65.108.231.124:12656,e387712543bc99c6719f7975ee75e48afb99b088@66.45.251.38:60656,dbaf54296be069236a31a3f23c0ed653deadb9b2@188.233.19.212:26656,4fb43c4d6bd6cf0f20781b67e437263a24e4153d@95.217.75.105:31656,66dd5faabd4e09ba6bc0ab0093392064f454827c@185.215.167.74:26656,a5091d1afa277bab864a495d43226ee44f85604e@212.23.222.91:39656,57cd99659f4895cada5ba5a9f594ce9a5fdb0fa8@46.4.23.42:46656,bce7435b6231fd97885ffccc57b1d7d98f20b37f@173.212.235.229:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,7e66e2984323a5c7de1967a6c7bd0931beb358da@89.117.62.163:26656,9a46a84b86410636540e7405e8d76ed4740b6bb7@46.151.26.153:26656,63256b5937ac438e3b21b570a07ace6ddc3bd0c6@194.163.182.122:39656,07d59fc815394526696a364ef4c6910683c332e7@139.144.97.186:26656,5ae4c8cc5763de7c105dd3dba66b7212328bced5@23.248.175.210:26656,59851a542633185cf7244fa4901ac832c5f5bcd6@45.10.154.247:26656,d3bacf8624684354d0676320bc5556e1e893bdfa@65.21.91.50:26656,aaff99ce425ac9d062d1bca6f75987656e137307@138.201.34.19:26656,e77e3503c9e83055b4f41ce6984f71fbbda46ef1@194.163.184.46:28656,01c22f232638ae4d534b097c2f91b8589a5be715@217.76.59.212:39656,10a2db5117fe9fdfefcfc9ca633e5633b0c38d4e@34.125.211.20:26656,9f06819b9ca5927310ffad266220ec2b1c2a0edc@82.165.207.203:39656,00abaa0b6be5c41bbb6a72315b301091481a8aaa@95.128.140.24:12656,b4583d9dd4dd03cda5f83b95edfd209f902de063@138.201.53.44:26757,8265b2067122eff44ca4fa11a46c3381c9034bc1@65.109.163.87:26656,0fd0b5cd2b6f3a0aca88e67c861c932cc0c8bedb@146.0.40.102:39656,4e3f67a4c88b40045e0de521bab5a3cee9aeb4aa@139.217.229.125:26656,a2d2ba190f32700f44e9dbe990c814f46abfc96f@81.0.221.31:26656,f41685745f7cd74caa542829d291367ae1377ce0@34.74.30.133:26656,78b41d73706a28af4e77c0c83b2ec8c36876b837@194.163.161.248:26656,cc5eac998dbd8d1c21ac293f1c946f1bb1583826@185.237.253.248:26656,c3f0e0e5ebad5bc97b9a9f563e20ae61f15f1f55@5.161.89.0:26556,b3d218f64916a94be981c33deda2123494de9997@94.16.109.190:26656,cff6880dd632d0d830b5bba47d1d62cd90c21ba9@95.214.54.56:35656,b6db16ab4d2dfd61d0be94df4738ce5f1913de11@212.41.9.98:26656,c171e9617904d5ab2ee7f7b5b58caab78154b703@89.117.18.185:26656,879d464755722009c853f748f04f729e4cd8b368@116.202.227.117:39656,be58621ecdf7dae1ff6fa5123793ddbc794427b1@65.21.248.137:26656,e9597b5074802ca53eb630a07603093e7ee98e6f@212.90.121.51:26656,e634fbf8800f76cb911d03e665f2e573188147c0@154.53.32.30:26657,9a5658a82838d6cea28c046dfd4fb605ca45b0ac@31.187.74.62:11656,d3ddfe8ad75847df085262b9cdbc49b29ce30ba6@35.229.110.80:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
