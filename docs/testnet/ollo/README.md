# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)


## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: https://ollo-testnet.grpc.kjnodes.com:443

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
peers="9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,771cfca799033e327511b25ae77784e02818d77f@65.108.101.4:23486,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,141456b9be6a468c262d126a275a804c7799f84a@62.171.143.40:23656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,fffb9164b9091d2055b5469a456ca91288517856@178.208.86.48:16656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,d915f25a07b79216e234e736f611b881d580f8b9@185.216.203.66:32656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,ef8863e006ba8eaea3aa8b780b01b82b401d7bd9@84.46.252.45:56656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,1e5d9db4138ed31ecf81b09365230d33360f8cde@65.109.81.119:32656,dfb2bba31436bc6cde54f475204ff53c9440804e@95.216.14.72:28656,412da32e046360f7e5168a89f80172ad093b17d9@65.109.37.58:17656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,1d576b61c0c56a9b6ef6dabf336fd3cf04c017b1@95.217.223.85:15656,b1c40c092d4c889d14ac8db36621c114f811d797@65.109.92.241:22046,da8d3ca8e1c147f0037b1c43ad3de7174f5ec1b7@209.145.59.224:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
