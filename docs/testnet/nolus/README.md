# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.1-testnet | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: nolus-testnet.grpc.kjnodes.com:43090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (40)
```bash
peers="37933575674b670c91a6aa336b1dd910057465a9@157.90.208.222:60556,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,73176af073e4f89609db7aa4ec3561ce1b98d308@85.10.193.246:32656,1c50df97e155afa50189f48daf41be046c7fe682@85.10.202.135:32656,3413989cce29fa5913eb149cbdee4ea5ee02b579@194.34.232.124:55656,0760923eff6e1e890a55e3c3d6b1330d60c2f870@185.246.86.152:26656,b19bd98f29fefc0c78e6b16b02e652a2148d3bfe@91.223.3.144:26556,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,0a9c575937847740cd9db495404ce12c225bb1aa@185.241.151.224:26656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,367fb20ca2380ebbb73eb19b772564383b0f37ee@65.21.123.172:26656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,79eea22837193c2b8e4d9ad1c633486f30faaa1c@144.76.27.79:56656,356a17fda44d7694cf8c3bf7a82491adea8536a9@38.242.228.69:26656,8d85b69ea7175ce0cf6ec7badae239339d6525db@81.0.218.59:26656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,91197362c5949e7c512783cd8e71b132551b1b2c@89.117.57.201:13656,fa0a2fe57c2ab28aee6cc0be4eddbc68d6587a75@95.217.165.189:26656,1e839449cac1898e98901a7d2c216c1a608c4e20@65.21.203.204:18656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,46e87e63ebfb628613a7c33ff69946ebd45fa510@176.99.142.180:36656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,e8473dede42e7f0d4668a24d909a5708c5a04a3e@65.108.78.116:11656,538e2a3d6e96cd7bc0635eaa3f8f3695f26503a7@65.108.104.167:21656,654e76e7d4b27fdb3a931fe2d44c51184d8a5731@5.161.78.48:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,3c043a562f432f367644c77b3d0dcc82e8143ec5@94.130.36.149:26858,6427076ade32a365c8cd888f40f24ea1dfbfea27@51.79.229.1:31203,ac86c1678e20a87bf2f036741932910869726337@135.181.222.185:15656,472e6f38168746ef24f87467323e9ca02883ad24@66.206.2.162:30656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,c86c29f1118891b1543c14f5833e6f26e9231a10@213.246.39.53:36656,1aed1013bdf53933c03498171660e5bda4c61103@135.181.158.36:26656,2e146ac9281e3797cbe1ad053e5ce6046b972c15@65.109.140.29:37656,84a5abdf6ce6f573ac1e3086ca693da6ec17c244@84.46.246.79:26656,f04c0c04bfffb27492286d5c4b0c6729426d0fe7@104.199.238.150:26656,5d323e4127ebf0c3139f3081765606e32052fa3e@65.109.92.148:26656,4c70dbb030c7b38e8f16999787074ed5ae33ba0a@94.250.202.17:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
