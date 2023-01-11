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

**live-peers** (24)
```bash
peers="3a178bcde0c4ebdcb933127e8440e49aafce894a@167.172.54.119:32656,34f4de6082a894a3b6addab6c370e62238d43649@65.109.28.55:28656,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,7dc63d58dccf6777206d5cdbc1ec1b9ba5221bd5@65.108.97.58:15656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,45c6c9060c390a068cf1d6c1d9999af196b961ef@65.21.78.153:30656,7b7c20db6602695b28297153b48aca884502439e@118.96.236.192:12656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,d4696aba0fbb58a31b2736819ddecf699d787edb@38.242.159.61:26656,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,44f506b0403a1226221bf8ad049ca1cf38d8b63c@173.249.7.166:23656,f246a18312ad72d95eab9858182eda632495be7c@207.180.223.195:46656,c83d2b5015c446e08f80c9d3662f4098077d635b@85.190.254.14:32656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,287523060f2046e921dd329bd97110967798edca@194.247.12.102:26656,dfb2bba31436bc6cde54f475204ff53c9440804e@95.216.14.72:28656,90ba3ab29147af2bc66a823d087ca49068d7974c@54.149.123.52:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
