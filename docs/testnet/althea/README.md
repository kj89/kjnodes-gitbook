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

**live-peers** (32)
```bash
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,dc67cbe058b802aa34f64715b44474c462b4317b@65.108.237.224:36656,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,22e7abeb10ac7042bce01c18d08958d9f3962a30@65.108.225.158:12456,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,5bad7ac6f006ee3b6f52dc91e85b5aae8e488233@194.163.149.53:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,d26fddea7ceb8cb5a52223702a23757cb09fad37@207.180.199.115:31656,c1ad743c152d67dea9df71e3de2024cddd57c0cb@31.220.84.183:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
