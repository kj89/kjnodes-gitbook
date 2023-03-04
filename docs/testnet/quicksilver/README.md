# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.4.0-rc9 | **Wasm**: OFF

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

**live-peers** (36)
```bash
peers="858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,bdb93c655989b2c1882339fabb013317066dda56@95.214.52.138:26676,a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,74abcb5243d4ffc43de6ad1a288d8e50adcd467e@65.109.80.176:20656,70c7663dba3b5181f1c3b8c92824dad070771ac6@217.13.223.167:56656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,b91f0ece92f0e2cc264176b29b51a6db886e020c@84.46.246.109:26656,1a178dec165fad14ab1b2fb6832dd092f6ab7a5b@65.109.23.182:21026,2be586e675b0f55c96905cc83496861c64112f44@65.108.99.224:56656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,2096650d8586b858d3369205f3b46ac4c765bc8e@65.109.53.155:26656,03332cdbc3d354846a18992effbb8c20aa28f52a@65.21.133.125:28656,ea7f3cbc25cb33ac75e4527abfffc921fcf55b51@51.195.234.250:26656,d1eea0f6a2b41757f7ba22e12235c0d7d6bb621c@198.244.203.194:26656,8ff8a186fe9cbc70d0f34891fa051f87e561a48b@158.160.0.93:26656,3c48a780b85d248e34e63eca5d44c624f93d09d5@135.181.59.162:11156,46f97e49a49694aead28c27be2c19300f509e273@65.108.129.94:26656,9e0604571aa20314c2261d70b7d8823414702715@51.159.141.209:26656,025e1a9ba7e536e1db47569b55081f7adf6d2f9e@95.217.83.28:26636,78d271e4b4692ff1ee8490f3825a541558b31870@65.21.95.46:28656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,78acdbabc08231765444b3143a222d433a5157e1@142.132.205.94:15651,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,1452d484454c0f93ddf3cbf987ce1b9cadd8f23f@65.21.95.180:37656,b06ee574cf0b8641611c709a36b21c103d968c18@162.55.245.219:11656,d4d83e209a2b096859821228ea17475f9a487a48@23.88.0.170:15651,97377c16946f8e1fa69e7c2c6b7feb32c2090f09@116.202.227.117:11656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,42f87cb55d5fdd222da28023613c66857398c4b8@5.22.223.252:26656,87d4e2b90141d5d52ed04387db4a46408c3fd66c@35.228.160.230:26656,1c4274460224753e8080d0efd16c0ed88fe27fc0@51.195.145.103:26656,f0621c59ca7cfba98015ae2a47886fc3d9c0020c@94.130.132.227:2060,f7edad3ff5a85d039e7de12067c63064c5b42d63@46.4.121.72:11656,a49d8d304e96350272dca24934b8295bc81d75d2@23.227.200.10:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
