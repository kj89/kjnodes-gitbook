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
peers="2cd7bd0bb40ed6f16ff7a9617ae8c7a74ce06e34@148.251.91.219:26656,bc55fa695313549672c4a480143dc400eaada16b@138.201.136.49:29656,bcec1c0df99526be43efa248491b87e8a2374ebe@94.130.26.9:26956,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656,6d97969912514e3583dee8e0cca15a383adbde6c@213.246.57.175:26656,019988ce47565ad683b7675216e8fbcb171b841c@107.155.125.170:26656,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,0d4220d2bbda711183a8db6f45c26b1541fa0d6a@65.109.116.204:21856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,c1d2d254a903b58692046b573dd06d2aa629266c@65.109.156.208:02656,76932bbeb29836c6405329c21358d051ef6e33a3@65.109.65.163:21856,17edf24237b1c2b5b196d344761f964407d05862@65.108.233.109:12456,2f43ea489479761a7cb7e250b634706d2a441c27@94.19.249.187:29656,04917b5810df2a380c1b18d83f577f1aba550818@222.106.187.14:53300,83147260a704b75283ca6da218516ee0eaa82956@170.64.156.36:26656,0037b2dc30933fa5c027a83be39f0061253ff83b@5.189.157.140:26656,311a410a9c7dcf7d074f75ce52f882ebae3b1bb7@46.38.232.86:17656,4f5eb5164329a61fc898ac75849ae873c8e539c9@66.172.36.135:14656,cc542d9fb5f93780fc4004aa67f2b502686a24e8@144.76.27.79:61056,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,1d9a103d1e24c590bdfb577537eddd19a322f886@65.109.92.240:17886,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,0aac1fc75b4a613f6bb7d15c6250350d478227a6@66.45.231.30:11144,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,938388d1a011858d6238bf22944ab2dcba9b22a8@65.108.199.206:36656,856ac01afa0163c27b69e1b25464427310120924@85.25.134.23:26656,5b6c6d679904ded86d36397e8ea583c122f5ddbd@144.91.102.95:26656,405320bf061e7c2ab22b72597f9f149e8a30f17b@5.196.7.58:26756,90d692d481c1c4739ba8a7045b5552fa8d410901@88.99.164.158:17886,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
