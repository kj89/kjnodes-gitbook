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
peers="e3d1fbe11462a128f14ebc10f7e8bd59823f09e2@161.97.152.215:26656,45c6c9060c390a068cf1d6c1d9999af196b961ef@65.21.78.153:30656,90ba3ab29147af2bc66a823d087ca49068d7974c@54.149.123.52:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,c0b03cf21640b12d78f6b4b50d7505d05d37f055@95.217.230.54:26656,84d57c8b3b4c07acc97e922cd17b8fc6dfa79a3b@142.132.152.46:26656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,ed38d885d068a963b0bc3986bb69680c34757a40@135.181.83.157:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,93085f2731cabd480d9b61397d3e1cf84f5a023b@168.119.124.130:32656,46d6f338d845f2eabf046d8bbabdab70a7d94b18@89.179.33.100:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,4da239f27366a2f0076163fc577afdc67d470a82@65.109.90.33:18156,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,74e60a35557efc793edb10667c3fff979ccbf49f@141.95.204.81:26656,90c1f1775c36690b04bccc08ef942add99826358@38.242.212.52:32656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,1e5d9db4138ed31ecf81b09365230d33360f8cde@65.109.81.119:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
