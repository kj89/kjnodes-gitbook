# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.6 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/uptick-testnet](https://explorer.kjnodes.com/uptick-testnet)

## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: uptick-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (42)
```bash
peers="a489dcbd4c5b7ef20d77c51dba217e85c631f463@65.108.105.48:20456,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@65.109.50.106:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,11995495f726f4e4c2ab74862fdb30e87c167448@65.108.195.235:27656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,94734f927b16ff91f5e45875396295d6173ca918@74.50.70.118:11574,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,dd8080d9ea1f3830370a4f51ca6fe858a3d32191@65.108.72.253:11656,878101ab9ad2402bfd700a3da58223778461c753@185.245.182.152:26656,49c86b1fdc3f99ac3108904aef4f64297f3f1415@209.222.97.81:26656,57876cfa3a101068885f302df69ff5556720af3b@154.26.137.198:36656,7a9b1f1ed80e854dfbf95f921c35f950f9278ea4@161.97.162.123:31656,f30bf0eebdd10788d09d5c64132a7161d714e126@154.12.243.189:31656,9d4d5e7c4f7c7cd0b7ef5fa580a0ea9e07f7bcc0@204.93.241.110:27656,e9fee55fdf6668e4e04927cdd85bbbbc9e9e43b1@209.145.62.101:26656,ad563c8036250cb34f3e822280ead9c59c9537d3@185.239.209.124:31656,0148cb2bb6b646cb147b1651ad503fcf9abfc652@107.155.98.194:36656,c6ca186e2ea0202a78b357c9b2d8883e3d96613a@144.91.110.211:31656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,aff8d7b78840eaafa6c2bafd9a76b76e565b2933@65.108.131.190:25256,a818920590d15226a206ec4c73b1c5c20c56a435@65.21.134.202:26666,3edfe380f7eff0658582c158f2eecebae2e0fed7@213.239.213.179:26656,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,45f58ce671967a10933ea3e2279be03f0ebcb42c@85.114.134.219:16656,5739ae6fab71ec95fb3112f4d1ea2845782fa9f7@54.92.137.6:26656,f58fd7ff25183e7e0dc3c35e667641129a8bc2cd@144.76.27.79:26656,e24bde7fe207160442fe6b93ee376a739def5757@51.222.248.153:26656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,dedd92019e364182bc24e7d4052fd7cefa94a976@65.108.200.60:20656,52cdb51fe8692dea11de23b8c97c9d947a6eb1c2@51.222.44.116:10656,b8e76d2223663e9bc47351564f1017b6e89deeee@95.165.89.222:24476,9fda526bd693e6b35a877a087f0061d4f20a7fba@65.108.108.52:20656,1bb6d67af0dd1d452e294e9df430d07bccefe502@185.215.167.241:26656,aa30d4d1748553c3619d9d9b1121df0b99de87b1@45.88.188.93:56656,aefbc6fea5a1a0eb0e0974a218e4748618d7ab2d@138.201.204.5:31656,a3b3712dfd366c5c39f6a6b3265c88c4166da86a@161.97.93.245:26661,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,02e89f27f64c1d097beb5929c3ada13ae4ce2828@2.58.82.181:26656,d42cf28de5fcf5786d78fce2936633c9eb927b2e@65.109.84.214:56656,2c952455a0e425081b54855091ab84c1fe73c4bc@65.108.231.124:10656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
