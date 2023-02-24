# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)




## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: [https://ollo-testnet.grpc.kjnodes.com](https://ollo-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (28)
```bash
peers="7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,fffb9164b9091d2055b5469a456ca91288517856@178.208.86.48:16656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,799dff05af5d30477f44c816753ff89104b2b8b5@116.202.227.117:32656,6a2e6873ad316bc45342ec3b79430657fe714233@209.97.179.146:26656,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,0ce58fd448e62aa0c06c2603d8e047b9c7f9a3e5@38.242.158.251:26656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,036d17d15c4e36cee8d93f9fb1a5ad5cb956631f@213.136.76.191:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
