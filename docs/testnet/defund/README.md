# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (29)
```
peers="507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,6bbd4d421c9610e918fee90a81278e689e445d81@194.163.184.53:40656,2ed9881acbe697281fbc6bf40e296c2dfa141740@178.128.26.238:26656,ccace1585ce7d671f09d4d442d77936b29ee8118@164.68.127.182:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,f516bd081b20c900d27fb6ca70991100845ad2b8@84.244.7.44:26656,71663397bb1d94d1b58af63cc2a0111bcabf01b9@65.109.82.75:26656,68b4a53b3b67da6a4736888c36074eb316ea510d@75.119.157.222:26656,f94f1daf71e3c2dd06ebbab0c2061fc723f8b539@190.102.110.86:26656,328b742040c36ed83efbd9a4b07c3bc0e3493157@62.171.158.158:26656,77a7c437c7e0c421eeaebe677235306d2466da4c@91.194.11.156:26656,f98092af7d5aa5fedb2af24200eb4ceeb252a007@91.194.11.115:26656,7b44ee4ac4dd29f7cd661868b77138e598218218@194.163.181.134:26656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,5ac40e96d9194536e15a28a1010551300cbab616@185.216.75.21:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,563a249cbdcccaaec6330f2914d92117c2d078fe@194.233.82.172:46656,8a865d76928017ad8e889b91b4d52bfb88526392@45.67.229.12:26656,90b3b7bdb4e58a91bd02b792ddd9015c1f2e177b@137.184.232.142:26656,7bd385047301b8a0caee30f9b99faa3e511c35e3@38.242.142.76:40656,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,f01417a2cb9c2e41e618576b5037c23975e95511@38.242.209.175:40656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,e2524d876035af6d361cf5f09146c22e67ea7ff3@38.242.140.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
