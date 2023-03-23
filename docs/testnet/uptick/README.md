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
peers="9fda526bd693e6b35a877a087f0061d4f20a7fba@65.108.108.52:20656,3cffe20d473b0bd4451d330da8b741b5d42dcb44@65.21.131.215:26666,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,5368bc0c12a7bfd9d69ba192b06f2be97d28e7ef@185.239.209.56:31656,52cdb51fe8692dea11de23b8c97c9d947a6eb1c2@51.222.44.116:10656,e24bde7fe207160442fe6b93ee376a739def5757@51.222.248.153:26656,49c86b1fdc3f99ac3108904aef4f64297f3f1415@209.222.97.81:26656,57876cfa3a101068885f302df69ff5556720af3b@154.26.137.198:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,11995495f726f4e4c2ab74862fdb30e87c167448@65.108.195.235:27656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,94734f927b16ff91f5e45875396295d6173ca918@74.50.70.118:11574,878101ab9ad2402bfd700a3da58223778461c753@185.245.182.152:26656,a489dcbd4c5b7ef20d77c51dba217e85c631f463@65.108.105.48:20456,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@65.109.50.106:28656,dd8080d9ea1f3830370a4f51ca6fe858a3d32191@65.108.72.253:11656,f30bf0eebdd10788d09d5c64132a7161d714e126@154.12.243.189:31656,dedd92019e364182bc24e7d4052fd7cefa94a976@65.108.200.60:20656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,9d4d5e7c4f7c7cd0b7ef5fa580a0ea9e07f7bcc0@204.93.241.110:27656,a818920590d15226a206ec4c73b1c5c20c56a435@65.21.134.202:26666,737e25ce01c94b20bdcb3d9ce642837ae7f4069a@135.181.116.9:31301,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,7840c994f5d84bf114ebb10ba704ded1c1bd12fd@65.109.112.20:11054,910b59a791d83dd35a5c2f1b99de2e6ae14591bd@161.97.75.5:26656,e05ef87e0f9a2940cf057aefde89abf8171b00fb@65.109.84.250:15656,b9e0210809b9dfc9cd299c6e83116d7fa45c6e27@65.109.68.93:46656,e9fee55fdf6668e4e04927cdd85bbbbc9e9e43b1@209.145.62.101:26656,b8e76d2223663e9bc47351564f1017b6e89deeee@95.165.89.222:24476,3edfe380f7eff0658582c158f2eecebae2e0fed7@213.239.213.179:26656,5739ae6fab71ec95fb3112f4d1ea2845782fa9f7@54.92.137.6:26656,0148cb2bb6b646cb147b1651ad503fcf9abfc652@107.155.98.194:36656,d42cf28de5fcf5786d78fce2936633c9eb927b2e@65.109.84.214:56656,45f58ce671967a10933ea3e2279be03f0ebcb42c@85.114.134.219:16656,29b9ad4e0eee5869a7bfc20bc3eecdfab668dc38@176.213.104.53:27656,01c911bce80bf11b786f107eaa8d48878ee71908@65.109.90.162:36656,0d97e3e88b7560c5169b1c69091ca2f9f22477e6@185.48.24.106:27656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,2c952455a0e425081b54855091ab84c1fe73c4bc@65.108.231.124:10656,34d28eeb7be1b245fd64ba2df4cdf62b5eb60dd3@202.61.240.155:30001"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
