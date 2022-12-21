# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


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

**live-peers** (29)
```
peers="7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,60a8fdd419c20f509cf590a10978827bcf1cf25c@161.97.99.251:11656,e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,46d6f338d845f2eabf046d8bbabdab70a7d94b18@89.179.33.100:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,0bd4dce54aad2d9b67b992fd69b51694b43d3272@149.102.147.59:32656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,84d57c8b3b4c07acc97e922cd17b8fc6dfa79a3b@142.132.152.46:26656,83c109aacea2db21f46f9c4c5dbb5a7cbc81e6e1@178.62.62.90:26656,b7026f21b05313fa5344a36977d2717f12613c35@138.68.173.189:32656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,e463f8ca93e10acf81964d845938e982c28c40f8@95.70.160.37:26656,fffb9164b9091d2055b5469a456ca91288517856@178.208.86.48:16656,084a8a6866edb7ed571e5b5f023be580e5673fee@95.165.89.222:24646"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
