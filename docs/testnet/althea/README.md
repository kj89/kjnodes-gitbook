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

**live-peers** (31)
```bash
peers="27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,d4c21f733f0aff703d36265b25126b01eaab8742@68.142.182.44:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,1991a3263255fc32d65b49335bcaee19f607c934@185.16.39.99:26656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656,a1c05be605625e7fd3af6b9e5c84937a48482be5@35.201.194.177:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
