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
peers="18643335ebbf1119ef5da9bbb2b65ce651a47ef1@5.9.106.214:26676,2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,27dc32e6a756ccb04ca4e1395008f18f5efeaf8e@162.55.1.2:31656,96320aaab7794933fddbc2bb101e54b8697c58e7@141.95.65.26:26656,856ac01afa0163c27b69e1b25464427310120924@85.25.134.23:26656,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,c215cf295b05c1338fdf5070a7b2abde873f5a88@95.217.40.230:26656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,70caf9545f6fd67f2561964b0a69bf36ba6f81d4@5.161.205.63:26656,bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,fd54b3d5e49c047dae61ca3a8e430f500eab783c@65.109.92.148:26656,8203297aacaea1d889fcf36240484c9efc217bbd@116.202.156.106:26656,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,6c3d7683bf40a521b7c22391fd6c989b46a2e0e2@78.46.106.75:27656,c5f4a56c4f1ba1cf3d4f8d787eb0f90d9cb963ec@65.109.34.133:61056,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,975393744d620d9dcb8dfd21c0282a6285766523@176.57.184.215:26656,733e9d5f995c2866df9f2e1254551940f060a70c@51.159.159.112:26656,382264d78149b62e679bf6d0b93dc74dd033fc05@65.108.2.41:26656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,3aeffaa1ac7b6741110987cfae4604751ac7d865@107.22.132.229:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:12456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
