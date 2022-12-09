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

**live-peers** (27)
```
peers="04621fd537750900278a4b7e125c7d148ef8d8eb@130.0.216.207:46656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,3e3dfe25eed3a5fb654887902e051a637b8d650a@185.188.249.246:40656,e3d98694b276a2fa3bd52a77d00d379f0aacb58c@173.249.7.166:26656,2f78b32d1f54bfa9342a909f31e3cfe4b4a3a417@161.97.145.238:40656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,328b742040c36ed83efbd9a4b07c3bc0e3493157@62.171.158.158:26656,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,abeb7b59282d3220aceca9b3a13c98021e6419a4@161.97.66.90:26656,1b3da07eeacc2b4d41eb1e1aac3c74244b9fa86e@167.86.115.193:26656,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,68b4a53b3b67da6a4736888c36074eb316ea510d@75.119.157.222:26656,e9d046b2248e07896dce1bcc5faff02d65745332@95.111.254.87:36656,8a43a51cb31fce7538e63f7e8b2d5350dbfa0c87@109.123.247.51:40656,86cb9d6fc8edfb8eac1feadfe05cf3f9e00810df@193.57.138.24:26656,8a865d76928017ad8e889b91b4d52bfb88526392@45.67.229.12:26656,563a249cbdcccaaec6330f2914d92117c2d078fe@194.233.82.172:46656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,f94f1daf71e3c2dd06ebbab0c2061fc723f8b539@190.102.110.86:26656,feecdf46334d46bb22dc041ac93e0f2c41a7d71d@38.242.209.148:40656,f01417a2cb9c2e41e618576b5037c23975e95511@38.242.209.175:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,26cf08ed9aa7fa3d940105ec773f08487b8d945a@190.2.146.152:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
