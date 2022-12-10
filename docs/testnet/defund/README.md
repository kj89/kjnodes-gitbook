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
peers="20b23961a22091e2a5047482d84bffacb49f416e@199.175.98.110:26656,abeb7b59282d3220aceca9b3a13c98021e6419a4@161.97.66.90:26656,6ad4f3be13155729927f0af19ceb08f89477798d@75.119.131.75:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,86cb9d6fc8edfb8eac1feadfe05cf3f9e00810df@193.57.138.24:26656,ace832f2bc1f52da79d5bc90a625184564ea2cd4@149.102.143.214:40656,64983f6c05304957ba9cce53173e571e6731cf75@130.185.119.129:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,2f78b32d1f54bfa9342a909f31e3cfe4b4a3a417@161.97.145.238:40656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,ca5db1a4d8d749131398e9580985e355bccf6504@109.123.241.109:26656,ce919107c495d85a20d37bb599bff42d843e4bac@45.144.29.185:26656,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,a0c14b06059dbcec81366a4581f3c25144baabed@38.242.194.202:26656,4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,77a7c437c7e0c421eeaebe677235306d2466da4c@91.194.11.156:26656,312e78a4ba124a1cc92f71d37a603c425ceb4d1b@199.175.98.108:26656,254da4ac248771ded96df539f7f70abbae5c3d93@161.97.77.186:26656,bbad6ab103461d0c2d2be18f8f304bdd90d46811@143.198.209.83:26656,6bbd4d421c9610e918fee90a81278e689e445d81@194.163.184.53:40656,b6b02b635b447eeca53c900d595cb6114a6e7f67@84.46.250.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
