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

**live-peers** (23)
```
peers="4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,934faf3a6108f975436b40a13a427c3fd2a82943@109.123.248.234:26656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,1ff7bdc7ba9ac6d66ef298956b7d11b5f84a15df@194.233.73.34:40656,e9d046b2248e07896dce1bcc5faff02d65745332@95.111.254.87:36656,ca5db1a4d8d749131398e9580985e355bccf6504@109.123.241.109:26656,20b23961a22091e2a5047482d84bffacb49f416e@199.175.98.110:26656,0045d87f68589572f2619eee220e513151f0eb92@155.133.23.28:26656,68b4a53b3b67da6a4736888c36074eb316ea510d@75.119.157.222:26656,abeb7b59282d3220aceca9b3a13c98021e6419a4@161.97.66.90:26656,6bbd4d421c9610e918fee90a81278e689e445d81@194.163.184.53:40656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,77a7c437c7e0c421eeaebe677235306d2466da4c@91.194.11.156:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,b50363075f36fa3382f78bdbe0c297dd27465eeb@154.38.161.212:26656,5ac40e96d9194536e15a28a1010551300cbab616@185.216.75.21:26656,8a865d76928017ad8e889b91b4d52bfb88526392@45.67.229.12:26656,2f78b32d1f54bfa9342a909f31e3cfe4b4a3a417@161.97.145.238:40656,e2524d876035af6d361cf5f09146c22e67ea7ff3@38.242.140.51:26656,19b298459704db74ac902caee55e3736a5147441@161.97.72.9:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
