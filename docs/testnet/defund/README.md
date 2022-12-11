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

**live-peers** (32)
```
peers="4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,d4f3f4cc8e170561eee79ae327784d20afb01ea3@65.109.85.52:36656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,c0b96875a8d2b8ff587c618e388ab3268bb586bf@154.12.246.0:26656,563a249cbdcccaaec6330f2914d92117c2d078fe@194.233.82.172:46656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,8a43a51cb31fce7538e63f7e8b2d5350dbfa0c87@109.123.247.51:40656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,ccace1585ce7d671f09d4d442d77936b29ee8118@164.68.127.182:26656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,ace832f2bc1f52da79d5bc90a625184564ea2cd4@149.102.143.214:40656,e2524d876035af6d361cf5f09146c22e67ea7ff3@38.242.140.51:26656,7bd385047301b8a0caee30f9b99faa3e511c35e3@38.242.142.76:40656,f98092af7d5aa5fedb2af24200eb4ceeb252a007@91.194.11.115:26656,312e78a4ba124a1cc92f71d37a603c425ceb4d1b@199.175.98.108:26656,abeb7b59282d3220aceca9b3a13c98021e6419a4@161.97.66.90:26656,989c2419816cc187213cd604d09b088b4d64518c@195.3.222.189:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,6b078e794479993cdcf4a44fd03f48ed107405b9@135.181.207.57:26656,ca5db1a4d8d749131398e9580985e355bccf6504@109.123.241.109:26656,3e3dfe25eed3a5fb654887902e051a637b8d650a@185.188.249.246:40656,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,f329bee02e530e05a8937887c8ea4e75851281f1@194.180.176.126:26656,6bbd4d421c9610e918fee90a81278e689e445d81@194.163.184.53:40656,028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,feecdf46334d46bb22dc041ac93e0f2c41a7d71d@38.242.209.148:40656,f01417a2cb9c2e41e618576b5037c23975e95511@38.242.209.175:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
