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

**live-peers** (37)
```bash
peers="24ae39234e1ceddc1585af9be8a6484edac79123@49.12.123.97:26656,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,874f5688891e0a273fcb2e3fb89af2f1ab700024@91.223.3.144:26456,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,856ac01afa0163c27b69e1b25464427310120924@85.25.134.23:26656,bdf94092f6dc380f6526f7b8b46b63192e95a033@173.212.222.167:29656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,c1c28d02ef687f2d80b8e4540d9297835e75b6f0@139.59.67.156:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,ff3fe47b494b0bf3dedf2d47dc9acf0e2ba3b7ae@65.108.43.113:52656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,698edcaf59b14f7bf50b681ef1ee3046fa062c77@65.109.92.235:11056,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,e5990247cc7fde4f94b44f687e0a9bda84fffe55@141.94.193.28:55766,c6e1ed7117cd56036cc51835945d155e9c474c01@144.76.17.123:26656,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,c831cd6ac278ab971eca94dda0c29191e8f39036@138.201.135.123:26656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:12456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
