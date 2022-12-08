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
peers="507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,0544670a43be0a61c7e354bc55d32b6573dc31cf@94.131.106.79:26656,6d8b87ae21e5eb44b8583d34a6b4867326c56a09@38.242.129.127:26656,20b23961a22091e2a5047482d84bffacb49f416e@199.175.98.110:26656,ca3658a2f24d0340e5eefce8c6c04e706188f407@38.242.244.56:26656,0045d87f68589572f2619eee220e513151f0eb92@155.133.23.28:26656,e3d98694b276a2fa3bd52a77d00d379f0aacb58c@173.249.7.166:26656,f01417a2cb9c2e41e618576b5037c23975e95511@38.242.209.175:40656,26cf08ed9aa7fa3d940105ec773f08487b8d945a@190.2.146.152:36656,9f6c7b49671054ec7d3960b33da1c5f6b66eac63@155.133.23.26:26656,bbad6ab103461d0c2d2be18f8f304bdd90d46811@143.198.209.83:26656,2997819a47da2666714f1c0d675c0041d42682b1@94.103.91.239:26656,672d909da12220d28d4c63e45c66b764c2d0b5f4@84.46.242.63:26656,04621fd537750900278a4b7e125c7d148ef8d8eb@130.0.216.207:46656,e9d046b2248e07896dce1bcc5faff02d65745332@95.111.254.87:36656,e8fd4ce8e97ff75fd76934c0da242bb872d28ad0@199.175.98.109:26656,feecdf46334d46bb22dc041ac93e0f2c41a7d71d@38.242.209.148:40656,8a865d76928017ad8e889b91b4d52bfb88526392@45.67.229.12:26656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,312e78a4ba124a1cc92f71d37a603c425ceb4d1b@199.175.98.108:26656,ce919107c495d85a20d37bb599bff42d843e4bac@45.144.29.185:26656,265fa3921d4ad0686d37fc0d69e7751c2cc49d3c@149.154.66.229:26656,86cb9d6fc8edfb8eac1feadfe05cf3f9e00810df@193.57.138.24:26656,b6b02b635b447eeca53c900d595cb6114a6e7f67@84.46.250.215:26656,f516bd081b20c900d27fb6ca70991100845ad2b8@84.244.7.44:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
