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
peers="0bee9e500e51465917506b47691a8fb032100da9@94.130.200.168:32656,b5f55cfc7b4d19f2dd3cdc71795f5a81e2c67f96@38.242.232.72:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@162.19.238.122:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,29b78da822388df177f4111e6589958d9f796f06@65.109.122.105:60856,67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,69d2c02f413bea1376f5398646f0c2ce0f82d62e@141.94.73.93:26656,6a2e6873ad316bc45342ec3b79430657fe714233@209.97.179.146:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,80c6ccc9523bd59a0420e76e8355f46fb61bf74f@65.109.93.58:33656,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,e53eedfc4c5c4487e1fba7f3b97de6aadfca8cea@5.161.179.64:26656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,ef2b392423003fe81c92ff8de2d08febc19b220e@142.93.36.7:26656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,d94c9bf688c921319bf3747e41cc6bafd589ffde@65.21.134.243:26677,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
