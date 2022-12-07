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

**live-peers** (24)
```
peers="26cf08ed9aa7fa3d940105ec773f08487b8d945a@190.2.146.152:36656,bb25b67fd12c5b08b6d949eb21d1a3a865307e1e@95.111.243.155:40656,e9d046b2248e07896dce1bcc5faff02d65745332@95.111.254.87:36656,19b298459704db74ac902caee55e3736a5147441@161.97.72.9:26656,20b23961a22091e2a5047482d84bffacb49f416e@199.175.98.110:26656,aa0f97cda5bd962821b907245dc476348309fce3@84.21.171.33:40656,abeb7b59282d3220aceca9b3a13c98021e6419a4@161.97.66.90:26656,30bfb2032cf377bdf0281807fdf56d1f6ef49802@65.21.104.54:40656,8a865d76928017ad8e889b91b4d52bfb88526392@45.67.229.12:26656,6d8b87ae21e5eb44b8583d34a6b4867326c56a09@38.242.129.127:26656,f3750b51cdf108c5a4c42016e5aa8225ddc48dc1@207.244.245.41:26656,4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,2997819a47da2666714f1c0d675c0041d42682b1@94.103.91.239:26656,b6b02b635b447eeca53c900d595cb6114a6e7f67@84.46.250.215:26656,312e78a4ba124a1cc92f71d37a603c425ceb4d1b@199.175.98.108:26656,f01417a2cb9c2e41e618576b5037c23975e95511@38.242.209.175:40656,1ff7bdc7ba9ac6d66ef298956b7d11b5f84a15df@194.233.73.34:40656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,f516bd081b20c900d27fb6ca70991100845ad2b8@84.244.7.44:26656,328b742040c36ed83efbd9a4b07c3bc0e3493157@62.171.158.158:26656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,324c36dcc39039d6c8007711b5923b4645c93202@142.132.202.50:46656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:10756"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
