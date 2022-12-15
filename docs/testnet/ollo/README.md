# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

Website: [https://www.ollostation.zone](https://www.ollostation.zone)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (27)
```
peers="412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,56bd2e7676dc6153c044701057977c6f0475b847@38.242.150.136:32656,d5b72f42a88b60846d8c1884652bd87a4ffa0017@65.109.27.156:34656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,3baa3ab28418101d74a75e859b7ac0777f671c1c@65.108.204.119:26116,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,1cb68888ccf57fc37edd40908b5e8ea810c3a64d@84.46.246.109:15656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,46d6f338d845f2eabf046d8bbabdab70a7d94b18@89.179.33.100:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,5f2e17783db19bcf868b03a1ee0a6e2cc47df6d3@185.16.39.3:26656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,45c6c9060c390a068cf1d6c1d9999af196b961ef@65.21.78.153:30656,4b73754c2c10d523ffd43ca95d9cb6e0ad8204a4@5.189.148.147:26656,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,0bd4dce54aad2d9b67b992fd69b51694b43d3272@149.102.147.59:32656,90c1f1775c36690b04bccc08ef942add99826358@38.242.212.52:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
