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

**live-peers** (25)
```bash
peers="9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,1cc735dffbe3861336f07bf9f1bc29c42e0e4a55@37.187.78.201:32656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,0d642afa8df369a5021609c43bb7765a332a615f@65.109.106.91:17656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,a9123ae1e1b7f8438e7262efd50031aab600df41@154.12.225.160:32656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,7db2f25b3bceeb32769d20316d5f1567f0a4bb54@167.86.99.7:16656,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,e709b708ea24ed8fefb5c82cc460bb485b403960@83.8.127.9:28656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,032845b1a798108bfc1fd91ebe5bdbbccd4a34d8@135.181.221.186:32656,90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
