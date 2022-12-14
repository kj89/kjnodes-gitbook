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

**live-peers** (28)
```
peers="028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,9a88a8643a1e0641f81c65f0ace6d0d44644dc37@162.55.211.136:40656,9e3c8603f8eb1aeacf7392701a1977668684803c@194.163.170.245:26656,dc8661d36681b73cf4dfde1d68587aec88212344@154.12.225.113:40656,bb25b67fd12c5b08b6d949eb21d1a3a865307e1e@95.111.243.155:40656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,6bbd4d421c9610e918fee90a81278e689e445d81@194.163.184.53:40656,e9d046b2248e07896dce1bcc5faff02d65745332@95.111.254.87:36656,7bd385047301b8a0caee30f9b99faa3e511c35e3@38.242.142.76:40656,19b298459704db74ac902caee55e3736a5147441@161.97.72.9:26656,563a249cbdcccaaec6330f2914d92117c2d078fe@194.233.82.172:46656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,328b742040c36ed83efbd9a4b07c3bc0e3493157@62.171.158.158:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,b3ea7a581e2f1c1e19d2067e6cd54497914ec4ea@173.249.54.237:40656,f516bd081b20c900d27fb6ca70991100845ad2b8@84.244.7.44:26656,b6b02b635b447eeca53c900d595cb6114a6e7f67@84.46.250.215:26656,3e3dfe25eed3a5fb654887902e051a637b8d650a@185.188.249.246:40656,aa0f97cda5bd962821b907245dc476348309fce3@84.21.171.33:40656,f17140ac29380d434c1b5d2e33798d9f3bc6fd45@209.126.2.211:26656,68b4a53b3b67da6a4736888c36074eb316ea510d@75.119.157.222:26656,e2542af1f83025786c34947f1b6d39a511500327@173.249.20.104:26656,f98092af7d5aa5fedb2af24200eb4ceeb252a007@91.194.11.115:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,254da4ac248771ded96df539f7f70abbae5c3d93@161.97.77.186:26656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,be4a0baa86b3d3bb2aba2defe1877fdc5cc7bd85@45.147.199.41:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
