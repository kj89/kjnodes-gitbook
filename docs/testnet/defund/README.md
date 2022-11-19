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

**live-peers** (33)
```
peers="2c4ddd8d4af5405618098648864d1d9975024aa3@95.216.173.157:26656,fe32ed5f0a7f8928f8299d8dd78fc5b650472ac4@65.108.46.123:56656,fd2122d21e10253a86739bdd33686065008926ed@85.10.200.221:29656,7da687fa5a1f9a635fb333519582fcc6fdada112@135.181.89.99:36656,028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,83902507559b71918fbeeb54ccb31411917c219d@135.181.25.153:26656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,75e38d35a430a9c1ac65249db3d4cab245159a8b@144.91.97.124:26656,16af5142a97d6bd22f941c15ad8faf2150d48e59@157.90.157.18:26656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,e6b3dc37e08c1807cc044eb56061cfe0186af569@65.108.206.45:27656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,2997819a47da2666714f1c0d675c0041d42682b1@94.103.91.239:26656,d3a1d3f0bff49ca0356f4acf790234cc2c1aadcc@65.109.6.115:26656,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,897e47992933105fd3c466021eaa347225edc5b2@45.147.199.48:26656,63f84e13148befd235d28b3e46b1de2da0aa99d8@176.9.167.181:26696,50ab3cea5a763fed15f18dff1f35a503f88994b2@193.203.203.27:26656,989c2419816cc187213cd604d09b088b4d64518c@195.3.222.189:26656,9dd904e70deef1042fc8a0802381fb083f83dc39@5.199.143.159:26656,2d3d11ac1f96ffb54c1df3000ed1c73684507a3b@144.91.80.32:40656,7e936b2c89d1d1a757d262bc64f981ed48fb50ec@65.21.3.229:26656,760bc7fc66c15c9f2b9d722b9ee673cbdd265614@144.76.97.251:31256,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@168.119.227.28:36656,b3a1fda2347ffc225121793b91edd132abdcc2d9@45.147.199.63:26656,bef3701487b54ba73de5e0d84ac57fc2a54f3a5f@45.147.199.67:26656,89944fe8fc90920cdd95ac8b752b81524c357961@38.242.234.75:26656,cd53ab15aa53f7fd0f584bb60b253a4d53246867@93.189.30.116:26656,f657421825c924c583994fa0e4543b613519ca50@45.147.199.6:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
