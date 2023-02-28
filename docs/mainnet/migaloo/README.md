# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/migaloo.png" width="150" alt=""><figcaption></figcaption></figure>

The Migaloo chain is a permissionless Cosmos SDK chain on which  projects are encouraged to build their applications. Migaloo chain  is the home of the White Whale dApp, Interchain Command Center.

**Chain ID**: migaloo-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://whitewhale.money) | [Discord](https://discord.gg/AyvcgD4jy3) | [Twitter](https://twitter.com/WhiteWhaleDefi)




## Chain explorer
[https://explorer.kjnodes.com/migaloo](https://explorer.kjnodes.com/migaloo)

## Public endpoints

* api: [https://migaloo.api.kjnodes.com](https://migaloo.api.kjnodes.com)
* rpc: [https://migaloo.rpc.kjnodes.com](https://migaloo.rpc.kjnodes.com)
* grpc: [https://migaloo.grpc.kjnodes.com](https://migaloo.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@migaloo.rpc.kjnodes.com:49656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@migaloo.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/migaloo/addrbook.json > $HOME/.migalood/config/addrbook.json
```

**live-peers** (42)
```bash
peers="f7dede5bd05eb9615c8c6fa273e25bd4f10f56b8@65.108.109.240:3000,0326c9ee117587b7ebe3b26b00820642a8cf48ff@65.108.238.102:20756,aba0c3f98fb5bef1a0d991b8e2b8bba24f9908b6@65.108.111.236:55736,f4cada0792353a16093ea9ecb872cb5962ce01ce@65.109.71.210:26656,e39876398a43c0f9b93b5a82d8e38fa57c0373b5@65.109.89.19:20756,d23d14793da108b107ac809f5643d5bbbbbcb6a5@65.108.75.107:46656,175ca82ab5b282549d68d79ff2c3703d26bcacef@141.94.109.71:20757,32eed8c4079201b143d92860c9146b1d9e126aa2@168.119.89.8:26656,dfe5f91f824880e19d47475546d9874e0f2cea8c@5.79.74.229:8095,d8aa44568130ec24f953ce12708cb3ea72763cf5@88.208.241.28:26656,3b3428d679faa1bd498b3554ca798de3a0d802c6@162.19.89.8:20756,81eefc4de6acec31ccdd519d53270be024e4fe68@51.210.223.186:7095,78f0f5aa89b7ed92a5728dd3f67f646d8dda5213@198.244.228.162:55736,0c38efdc028867765e68f02979958468384ad087@51.89.155.2:23656,9780ea85f4d0f4cb5ebca14992ce11ebe1982d35@188.172.229.26:26656,9c77e7e841e1e5231d0f793dfbe051e9cbb13747@94.79.54.137:16656,36e1c376a0c5da53382a8ccb081d6a3e4831d165@65.108.234.59:26666,8a9e42026a687b2762cefbd74584ccbd6afa0be1@65.109.83.124:26656,80be85c4980deccaa2fbd710029f0eb660dadf9a@51.81.16.186:26656,e91f650bb3d5b66762093150718af358c6355cc5@15.235.10.35:36656,c616069071f0864b5b0e995f8d8961536b41ab62@15.204.141.36:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:49656,98e489fc375c4dd26eb0d2410fab4e1ab049f61b@144.126.141.236:26656,dfb44159d26b62affd7112367e082b2397bbff15@65.108.136.206:26656,347e6fa3c974e91aee92da5793486ba3f1bae67d@23.88.112.67:26656,9f55d181ba68c2a7b62d065fa5974bc1ada7395f@188.165.252.51:26656,59c74642d0ec4d012dd7bd0a7e5af1eadf2061b2@65.109.30.183:26656,1d3809b25bbe6a29bc2415df77c9fc82e46fd384@18.117.74.187:26656,e9e11032398b32a2dc6cc38b39bd81eb9125ed4d@65.108.97.58:2426,6870906f86e474d88d077c7c55af36debe49da04@178.162.165.194:7095,95a68d5280d9a3ae6d688e89bd4e4fe295b11a92@31.156.88.34:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27096,ba6f2c1a1174fbc19e1fff75922f56c779d788d8@38.146.3.131:20756,320ec920b1c1adc94556f9f64eeb575e07ef9d27@24.158.14.210:26656,ccaccdf6bafcb57197d86a1420a289cd39fe0ae9@85.10.200.231:8095,45a88789d86553f6cd7c7ee48786847e462e7dd6@5.75.161.219:26656,45c246b7f17bb9d95a3155e53ae32850de03d946@195.14.6.2:26656,a834ef7ec0a65ac7c5bf976a9af5adb3a71d7a19@65.108.8.247:20756,6c42aacf3939d503bad695d86108d214680e04a8@144.76.175.189:20756,20a8ee3728b358f9de624febd85464eb89dddd37@63.225.118.133:36656,4236750928a4dcb742e50e30e500ebc9ee39f240@35.223.246.103:26656,9755cab2585a2794453a5b396ef13b893393366f@65.108.212.224:46678"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.migalood/config/config.toml
```
