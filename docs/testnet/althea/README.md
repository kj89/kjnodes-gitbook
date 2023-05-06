# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:15290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:15256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:15259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (33)
```bash
peers="2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,dc67cbe058b802aa34f64715b44474c462b4317b@65.108.237.224:36656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,ee22e048af133e8e83d594314a67b89be964eb37@138.201.225.104:47856,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,13747f1f9960d19b72610cf7b59c2ec6d4eca27f@103.107.183.89:52656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
