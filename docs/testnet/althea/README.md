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

**live-peers** (31)
```bash
peers="aa500219761eecd7f1f02a8bfd21c6dcdbd3cf42@142.132.232.40:26656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,3f9a20277d68b7fe52efbe84dad231af472d0190@162.55.235.69:29656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
