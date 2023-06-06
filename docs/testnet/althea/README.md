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

**live-peers** (30)
```bash
peers="6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,31e4e58aed75f099eb5b71fd9fd48b48e4bf721a@5.75.170.207:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,7a69ca211e4dca2c8c5e5ad2582e81db6adb9f3c@65.108.70.119:29656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,a1c05be605625e7fd3af6b9e5c84937a48482be5@35.201.194.177:26656,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
