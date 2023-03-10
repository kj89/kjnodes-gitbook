# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quasar.png" width="150" alt=""><figcaption></figcaption></figure>

Quasar (pronounced QWAY-ZAR) is a decentralized  appchain enabling interchain digital asset management.

**Chain ID**: qsr-questnet-04 | **Latest Version Tag**: v0.0.2-alpha-11 | **Wasm**: ON

[Website](https://www.quasar.fi) | [Discord](https://discord.gg/quasarfi) | [Twitter](https://twitter.com/QuasarFi)




## Chain explorer
[https://explorer.kjnodes.com/quasar-testnet](https://explorer.kjnodes.com/quasar-testnet)

## Public endpoints

* api: [https://quasar-testnet.api.kjnodes.com](https://quasar-testnet.api.kjnodes.com)
* rpc: [https://quasar-testnet.rpc.kjnodes.com](https://quasar-testnet.rpc.kjnodes.com)
* grpc: [https://quasar-testnet.grpc.kjnodes.com](https://quasar-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quasar-testnet.rpc.kjnodes.com:48656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quasar-testnet.rpc.kjnodes.com:48659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quasar-testnet/addrbook.json > $HOME/.quasarnode/config/addrbook.json
```

**live-peers** (38)
```bash
peers="8b2a6a1867136d22fe3615211675c5538217bca4@161.97.78.140:26656,be6acbd97513a61db028e51c9d380e7df0c3a278@213.202.219.160:29656,37470a0944d3b650e884e228d7c3732289cc8ed3@23.88.105.165:29656,fa198a8f2aab3c8c04f51fb293b9b95eb04c7753@217.76.57.186:29656,1236b168c2a84591e8a3db9faef590b65872fb75@217.76.57.205:29656,0d2f608cd0ec290432cc8d4452c1d44383c9992e@38.242.241.34:29656,7347025cb677ceeaa968998a6e46b9436774e1bb@217.76.53.47:29656,408f1be2d3b30a82bf7f1ce34cb2c20df68d200d@65.21.180.1:26656,fc15868d6bfc6b9199b22eb5ecea7a9aa347d8ed@65.109.128.186:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:48656,70addf3b7b4d749ca66f5d6e58c7084dd0e3dee8@47.147.226.228:56656,38cf4c8da13354be52a824a0a2d0db0f3884c312@5.9.70.180:15661,20af0bf9bdf951201cb6edc898e7e4c14c49435a@5.9.121.55:41856,08a99c97aa37bce18a9dd200c54f0420740251ce@43.156.74.181:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27146,a75c8d4db9f7159e73bb4abfc994086df0d11f25@209.126.2.211:29656,88f614e84a3642ea9e2d893f4e156b22bb11c106@43.156.130.99:26656,966acc999443bae0857604a9fce426b5e09a7409@65.108.105.48:18256,23380a58aa65b967170d52dfc3b8fd4201cd32cf@217.76.57.206:29656,4ffbe7674d924b8710743d44da923c29c2bb8bc6@65.109.235.186:29656,9c8de545052a9b4df47befb8f14b022f5aca5ed6@38.242.233.214:26656,a7d3bb039ce10a80c882ab2374182ac39c0af9f5@129.226.203.194:26656,f451153ab4eea029f58d4a5f48f67981f356525b@89.116.25.51:11656,9fd35fb5ac1e7f990dc99e01d189d9448f9d17ce@75.119.130.196:26656,fbdde323ace217badc53c4394a10272152f87c29@43.159.61.5:26656,e6fec75637dee245e3063a221f4f9511e0b2fc01@217.76.57.192:29656,4927ed1ac67cb02b20b72820db95086f85d087b3@43.156.116.43:26656,dba2e277cdf661dbfdc8d6f5dcc262a9e3fcfd59@43.156.101.16:26656,97a635ac14ab8ca116526ac100f316c589ce6613@89.116.30.72:26656,881db78e40385d87614cb847c2a19e8ead25b52c@43.159.47.25:26656,b63d8a5c9a7437301373c5d8b2162e0e464f5058@80.76.235.194:29656,22817c8f2da42e360d340d2bf910c648cbb31c47@161.97.79.100:56656,136589c157a21094c976f67bcb76bc6327c58b93@65.108.97.58:2686,7577c7a77cd79ac9e322cae9cefa2ba183d5e7c0@111.113.133.39:26656,47ced1ad4be0c7953085f69ff5a351187cd0aabe@161.97.92.139:53656,eeb4f094eaa62841b4a9a73f0560d6aa1fa87482@65.108.231.124:29656,8b8e7f5f4bb58d0aa0c2a171a454d0e02d800e3a@129.226.214.48:26656,50ee9fb6b3c3f7e5333364cc009ba0306098becc@43.156.117.129:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quasarnode/config/config.toml
```
