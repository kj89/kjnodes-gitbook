# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" width="150" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:52090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:52656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:52659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (32)
```bash
peers="ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,c1d2d254a903b58692046b573dd06d2aa629266c@65.109.156.208:02656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,79d18c52d35ddd204f61e9be8aa3c7b35d75cab7@65.108.139.20:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,4a8c845bdffc8bae0ed0e91a476bc57720adec15@65.108.206.74:26656,1f1d115b9a70aa72f321bae376b1c6e44bab4668@24.17.14.167:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,766377592cbaae65d8e6df5120bd8b4fdfc8a372@98.63.20.2:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
