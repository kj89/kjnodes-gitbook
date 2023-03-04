# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (38)
```bash
peers="eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,7849e4320385434b0828a3e0206a3b69767393f6@65.109.91.227:26656,b9d3fe835ded0b93c39befad43fb3c4964ae740f@91.195.101.100:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,7dace139a0389ca95c5eda64ddf19a01e6d60d02@95.214.52.206:26656,5739ae6fab71ec95fb3112f4d1ea2845782fa9f7@54.92.137.6:26656,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,11995495f726f4e4c2ab74862fdb30e87c167448@65.108.195.235:27656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,5badbf826e75a2afc216023dd2e7b8ad0eeb9fa6@136.243.88.91:7060,fb2308819cefcdd8a74e957f82156625c47c42bc@65.108.229.95:26656,94734f927b16ff91f5e45875396295d6173ca918@74.50.70.118:11574,737e25ce01c94b20bdcb3d9ce642837ae7f4069a@135.181.116.9:31301,dedd92019e364182bc24e7d4052fd7cefa94a976@65.108.200.60:20656,e05ef87e0f9a2940cf057aefde89abf8171b00fb@65.109.84.250:15656,661e4acbdb446e543e5e86831b5750df829bc0e0@65.109.19.146:26656,d0a53deabbc668a5bade8fc8b92cb9b0cba48c94@65.109.117.229:36656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:18656,49c86b1fdc3f99ac3108904aef4f64297f3f1415@209.222.97.81:26656,a489dcbd4c5b7ef20d77c51dba217e85c631f463@65.108.105.48:20456,f58fd7ff25183e7e0dc3c35e667641129a8bc2cd@144.76.27.79:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,1cc42ab449f3e3877d8f69ad78182cf9e07c2475@75.119.159.159:29656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,e9fee55fdf6668e4e04927cdd85bbbbc9e9e43b1@209.145.62.101:26656,dd8080d9ea1f3830370a4f51ca6fe858a3d32191@65.108.72.253:11656,00242af3dded97bb8380c9b9d98457ea7879e0c0@198.204.255.155:26656,0afb5ce897e69eec34fb32bf87f4a2f93f79e0b3@65.109.65.210:30656,a818920590d15226a206ec4c73b1c5c20c56a435@65.21.134.202:26666,09d3655a7cd649c276b698cd57fcff4ec39a176c@178.18.242.228:15656,b9e0210809b9dfc9cd299c6e83116d7fa45c6e27@65.109.68.93:46656,5279dd29f49dc5b0b27802af0d475294144c8e6f@65.109.6.21:26656,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,2c952455a0e425081b54855091ab84c1fe73c4bc@65.108.231.124:10656,bfc2be7e459b947973a15a01055cad86ad34f35c@185.163.127.24:15656,f97a75fb69d3a5fe893dca7c8d238ccc0bd66a8f@94.23.23.189:6969"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
