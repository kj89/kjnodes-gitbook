# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.3 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: https://lava-testnet.grpc.kjnodes.com:443

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (38)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,c19965fe8a1ea3391d61d09cf589bca0781d29fd@162.19.217.52:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,1cfea692eeabae3c4382d62179278e88ebd8d447@164.92.223.212:26656,ce67e9671e7212695a0a7ba27fb0c723ea6ccff0@35.225.146.131:26656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,07768e40d86ed4230933417764c16e36afc11492@173.212.245.122:36656,afc25b4b9f88c5af73c221475c47ba4c1cce4ae7@34.27.247.0:26656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,8024dd3fc948df4577ffac0dd1c44ecb8d9fff03@109.123.240.125:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,8ffa4dbef4c0b2a1dc1172760914e2df1468fb22@178.63.8.245:60756,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,2031e65ee8a13e57d922a14d28d67be0ada21a95@54.194.240.43:26656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,9f4d521f5115b5c43af3e7866e8a6e54e9afefe0@209.182.238.30:26656,82c3a20fbc0d18b0982b183fb535eee7e03a72c9@207.180.248.217:28656,443a5a86178f3d47fddc60c189c4a10b1840ed81@176.124.205.33:26656,0edff7d96af15cb031f41dacd2d6f3c968fe74ec@38.242.232.35:26656,0496ae158ae816b7a427b9f0be795db756952901@95.217.58.111:28656,910c0e9e8299d642208ef4c4199ae9ea44d6ffe1@164.68.99.218:26656,695f9e8dad50fa524ed96c4d5df7afe12963995f@65.108.124.219:38656,887df0564ab6ab74d18c9ae61e6afe6284c04b68@34.235.116.70:26656,895075f035b3720e93bcae0e08436d1782ee5472@88.201.169.176:26656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,8f6c7aa24b0f928109aa04f992da441b337c796d@38.242.226.106:26656,60be50fae1525143ea9226eff17830c4a474af6c@154.53.39.80:26656,ff7dec6f76dbcdef2a28f9a6c815de36cb26ea37@89.163.155.122:38656,97a7c2941a5875ce518f4775b841ff3b888c82d4@65.108.129.104:21656,c83d7b205b2e80bd9a33c13161bd39d520988455@38.242.139.189:26656,10b0118f5c1264ac7b9f45931717fef401530867@178.54.78.180:36656,ade02cddf71489b79a2054a7c6ba2cab8a0abb18@185.163.125.232:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
