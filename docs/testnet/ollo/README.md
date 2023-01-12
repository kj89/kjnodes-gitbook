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
peers="67d27bdbc3c444c557d555164518d8f551a922c5@136.243.103.32:46656,47655c33bdecae7f449301197d8b951a97e1b680@89.58.59.75:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,2a8f0fada8b8b71b8154cf30ce44aebea1b5fe3d@146.59.116.136:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,43da48176665407ebbe40f809a0ec2c84ab0579e@65.109.24.121:26656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,a99fc4e81770ca32d574cac2e8680dccc9b55f74@18.144.61.148:26656,8c4a28db4a9f4a37725d504d6f87fb5e1aee0266@49.12.216.13:46656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27006,e8bdc07477c4a49acf1a4c91e3dc34fe2372169e@161.97.153.160:26656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,a553ae4af55d127300dd707a46e715b47a82610a@65.21.131.215:26626,d5b72f42a88b60846d8c1884652bd87a4ffa0017@65.109.27.156:34656,1f06a05a88b812f9e8147379a2bb82c8bab37e42@84.46.252.55:26656,90ba3ab29147af2bc66a823d087ca49068d7974c@54.149.123.52:26656,7349272f712e713a957bf5349930e3439e98b518@167.235.27.69:20656,dfb2bba31436bc6cde54f475204ff53c9440804e@95.216.14.72:28656,15bcdea616c717eb4356e125d4f631aaa596dfd5@65.108.77.106:26929,c83d2b5015c446e08f80c9d3662f4098077d635b@85.190.254.14:32656,517786f9e5e9caf196fed64c2130528e0ef59643@65.109.70.23:18156,536c816c0d32ceb601fcf047284f65dc68c0513a@65.21.134.202:26626,42beefd08b5f8580177d1506220db3a548090262@65.108.195.29:26116,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:18156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
