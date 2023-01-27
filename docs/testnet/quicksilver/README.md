# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: innuendo-5 | **Latest Version Tag**: v1.3.2 | **Wasm**: OFF

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

**live-peers** (40)
```bash
peers="d40a714c11ea3040495246fa0ba8439fcff8a139@176.9.146.72:11656,af8cfa944802a9bd510fc3407950a15e8be86c31@213.239.217.52:30656,13564ca7ffcc8fa6bcc6d405c96fe8c724ec17da@88.99.213.25:11656,a1ef7f2e44f4be8e041f3a9e58cf58cd24b97e26@51.89.7.235:26650,858ba6bc33a6d13fdd9ddad344d788dcf91cf565@142.132.151.99:15651,41f7d7004cace7bd1760a5f980a86123700c8f1d@185.146.148.116:26656,9e0604571aa20314c2261d70b7d8823414702715@51.159.141.209:26656,a637b94cb989909cc182623748ef179b0659f148@65.109.23.114:11156,74abcb5243d4ffc43de6ad1a288d8e50adcd467e@65.109.80.176:20656,a37474c1f254cd4b16d924327a755c914e8e7d86@65.109.30.53:26656,46f97e49a49694aead28c27be2c19300f509e273@65.108.129.94:26656,d160a8908b44f2a44ce17e0be1f9056b58993b9c@65.21.139.170:21026,1452d484454c0f93ddf3cbf987ce1b9cadd8f23f@65.21.95.180:37656,8099f8a7c95c1676982e1a23e8452f2b10b07415@65.108.78.107:22656,ac0c6a8e9e700044226e9ff16b68ab4cbae6fb06@84.46.246.109:2366,42f87cb55d5fdd222da28023613c66857398c4b8@5.22.223.252:26656,521eabb3f5a0698476baf22c45aaef396399da10@135.181.183.93:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:11656,25b8b792bb14e8bfdcdfa163a14710d5645a4eba@148.251.91.77:20656,f0621c59ca7cfba98015ae2a47886fc3d9c0020c@94.130.132.227:4020,0551eaa0db7097274410ee27a71672817e314b83@167.235.245.191:26656,f7edad3ff5a85d039e7de12067c63064c5b42d63@46.4.121.72:11656,67224ac7f52eac4db6bb0a8de0bf8fbc5e7e0069@199.204.45.23:10656,a288baa951cbe92b253c01c3936d930af1d56424@5.161.142.236:26656,c133c4c0c7034c8c345330f394984ad08092fc14@138.201.17.11:27656,e0f0703e9ce343c46e0ec01b19216715e817b358@65.109.85.170:28656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.55.232:27026,cc745e98b4dc9b83c5a74d41f576feda73902dfd@65.109.38.54:20026,dc88be3a0075ce429a423237abe223a9528ce0df@65.108.204.119:31656,c9a74cdd754a8ccc9243ac2b245e4caaa78695aa@45.85.147.96:26656,3519e61e653db97f5d1c7f1bec9b0072bca4d5fe@144.76.45.59:16656,78acdbabc08231765444b3143a222d433a5157e1@142.132.205.94:15651,22a393fe9174c29081ad8aeaf14ce01b9a79d8c6@159.203.28.113:26656,dbe93dfe92d87db75463bd8b336e4a960fcb2235@51.195.234.250:26656,be637bd74973424c825c14c99b71f652fbabb48e@65.21.123.172:22656,3c48a780b85d248e34e63eca5d44c624f93d09d5@135.181.59.162:11156,4ccdccd18a480f13af85aa798356c1bf856f5c20@88.208.57.200:11656,0a3ac40a7a4ce35978c4da97be2eb6974bc3c58b@185.252.233.217:46656,e25a748120c9608c1d2a70fafa75178d862b3463@207.180.253.78:26656,4c24df4acfbaaf22e5f6f3c4d11ecf02e8cc343f@195.3.220.48:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
