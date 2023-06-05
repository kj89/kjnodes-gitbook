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
peers="6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,8cd0cf98fa86c01796b07d230aa5261e06b1b37d@95.217.206.246:26656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,eab7a70812ba39094fc8bbf4f69f099123863b38@81.30.157.35:11656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,16a9576c9a4cf9651b4215e3a877ae002555dd9b@116.202.117.229:31656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,31e4e58aed75f099eb5b71fd9fd48b48e4bf721a@5.75.170.207:26656,13747f1f9960d19b72610cf7b59c2ec6d4eca27f@116.96.46.161:52656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,26e70e13195b0d04cda0fca1f7b16b8746a620ed@65.109.28.226:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
