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

**live-peers** (28)
```
peers="e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,83c109aacea2db21f46f9c4c5dbb5a7cbc81e6e1@178.62.62.90:26656,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,cadc2b601a188aedbe4156a6eb5a81e00770bcfc@65.108.219.110:26656,46d6f338d845f2eabf046d8bbabdab70a7d94b18@89.179.33.100:26656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,84d57c8b3b4c07acc97e922cd17b8fc6dfa79a3b@142.132.152.46:26656,0bd4dce54aad2d9b67b992fd69b51694b43d3272@149.102.147.59:32656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,45c6c9060c390a068cf1d6c1d9999af196b961ef@65.21.78.153:30656,0ce58fd448e62aa0c06c2603d8e047b9c7f9a3e5@38.242.158.251:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,90c1f1775c36690b04bccc08ef942add99826358@38.242.212.52:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
