# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.4.0-rc4 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)




## Chain explorer
[https://explorer.kjnodes.com/quicksilver-testnet](https://explorer.kjnodes.com/quicksilver-testnet)

## Public endpoints

* api: [https://quicksilver-testnet.api.kjnodes.com](https://quicksilver-testnet.api.kjnodes.com)
* rpc: [https://quicksilver-testnet.rpc.kjnodes.com](https://quicksilver-testnet.rpc.kjnodes.com)
* grpc: [https://quicksilver-testnet.grpc.kjnodes.com](https://quicksilver-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@quicksilver-testnet.rpc.kjnodes.com:11656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@quicksilver-testnet.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver-testnet/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (24)
```bash
peers="0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,ee6bae1a6d4a1e07f1e4bc7963cabedc6b73426e@94.130.137.119:26656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,cfbf02b41e7fe78d51abfa93f342afd0687203c0@212.227.151.143:36656,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,46f97e49a49694aead28c27be2c19300f509e273@65.108.129.94:26656,d160a8908b44f2a44ce17e0be1f9056b58993b9c@65.21.139.170:21026,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,1452d484454c0f93ddf3cbf987ce1b9cadd8f23f@65.21.95.180:37656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,c4489720ba051c79f5bb16ae5d81341b0f248e19@34.240.190.194:26656,57b37e325cdfc0e2797cedb4102556bf5c3d45e8@51.195.234.240:26656,78d271e4b4692ff1ee8490f3825a541558b31870@65.21.95.46:28656,9434d151be05e013cb0f20d27b699c8272ec4c89@65.109.82.111:29656,ac0c6a8e9e700044226e9ff16b68ab4cbae6fb06@84.46.246.109:2366,934ee402c0ccda936b3d1e1a7876f76a45e88edf@65.108.44.149:20656,25410bff2fb7312d24c11b1e990507e5e3aa40b7@135.125.5.31:48656,926ce3f8ce4cda6f1a5ee97a937a44f59ff28fbf@65.108.13.176:26656,cc745e98b4dc9b83c5a74d41f576feda73902dfd@65.109.38.54:20026,78acdbabc08231765444b3143a222d433a5157e1@142.132.205.94:15651,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,e25a748120c9608c1d2a70fafa75178d862b3463@178.18.254.211:10656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
