# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.6 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)




## Chain explorer
[https://explorer.kjnodes.com/uptick-testnet](https://explorer.kjnodes.com/uptick-testnet)

## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: [https://uptick-testnet.grpc.kjnodes.com](https://uptick-testnet.grpc.kjnodes.com)

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

**live-peers** (41)
```bash
peers="eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,dedd92019e364182bc24e7d4052fd7cefa94a976@65.108.200.60:20656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,7840c994f5d84bf114ebb10ba704ded1c1bd12fd@65.109.112.20:11054,5badbf826e75a2afc216023dd2e7b8ad0eeb9fa6@136.243.88.91:7060,878101ab9ad2402bfd700a3da58223778461c753@185.245.182.152:26656,52cdb51fe8692dea11de23b8c97c9d947a6eb1c2@51.222.44.116:10656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,11995495f726f4e4c2ab74862fdb30e87c167448@65.108.195.235:27656,5739ae6fab71ec95fb3112f4d1ea2845782fa9f7@54.92.137.6:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,94734f927b16ff91f5e45875396295d6173ca918@74.50.70.118:11574,7dace139a0389ca95c5eda64ddf19a01e6d60d02@95.214.52.206:26656,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,57876cfa3a101068885f302df69ff5556720af3b@154.26.137.198:36656,61fc7df6cfcbe1403405a8ffe5b48f9b6ee75f28@213.136.86.80:46656,49c86b1fdc3f99ac3108904aef4f64297f3f1415@209.222.97.81:26656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,d42cf28de5fcf5786d78fce2936633c9eb927b2e@65.109.84.214:56656,9fda526bd693e6b35a877a087f0061d4f20a7fba@65.108.108.52:20656,9d4d5e7c4f7c7cd0b7ef5fa580a0ea9e07f7bcc0@204.93.241.110:27656,40a93c4be9e2dcb155d60e174c0e00d6808283e7@65.109.52.56:26656,0148cb2bb6b646cb147b1651ad503fcf9abfc652@107.155.98.194:36656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:18656,1cc42ab449f3e3877d8f69ad78182cf9e07c2475@75.119.159.159:29656,a818920590d15226a206ec4c73b1c5c20c56a435@65.21.134.202:26666,dd8080d9ea1f3830370a4f51ca6fe858a3d32191@65.108.72.253:11656,a489dcbd4c5b7ef20d77c51dba217e85c631f463@65.108.105.48:20456,132dcd9cbd5e6155edb535e477ba8262bb008243@199.175.98.113:26656,1da3e7446d53cdfc7f7170f7976b08964ec9b9f4@65.108.76.44:11693,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,e9fee55fdf6668e4e04927cdd85bbbbc9e9e43b1@209.145.62.101:26656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,bf3c106311f79ac69d7dd6adf57a632e03632cb6@209.126.2.184:26656,e05ef87e0f9a2940cf057aefde89abf8171b00fb@65.109.84.250:15656,2c952455a0e425081b54855091ab84c1fe73c4bc@65.108.231.124:10656,639831661a14e798a3928eb3abc0a6329a172e9c@65.109.112.178:28656,45f58ce671967a10933ea3e2279be03f0ebcb42c@85.114.134.219:16656,58cf2af0e94d7c55473a1e98225a6ff25baa0402@65.21.4.10:15656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,902a93963c96589432ee3206944cdba392ae5c2d@65.108.42.105:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
