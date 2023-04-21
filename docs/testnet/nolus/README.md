# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2 | **Wasm**: ON

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

**live-peers** (27)
```bash
peers="1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,6b14535ff005667f324f8439a55a21ee2f170d12@95.217.211.81:26656,b707384941f6ae2c291d7031b51771c470e3a686@65.108.9.230:28656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,b0fa31de7a29b92b4c910cbafb2789626a1db8a9@65.108.9.164:20756,e84c51a539d705787644e235faab6bccd4b73bdd@5.61.33.18:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,55efbf3711e104ada09b4dadba5890ea2a96d4b7@65.109.116.204:20756,228b1139c787fcb02358d99db748119123cf08c0@65.109.65.163:20756,f9734a35578309156308f12eba510ef995de4769@165.22.111.173:20756,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,8b0b427b4567a7a66f05fab1146ee97b52ad7958@93.189.30.119:26656,89d4b6b28f4399f49c82f9b0e891463f07f26cfe@95.216.65.177:29656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,b04b320e306ccd38b3da4d5ebc8099ceff452c65@178.63.8.245:61456,03ec7af23216082eeccc690b7bdcbe497bf2dcf8@136.243.88.91:9000,aad36d817f6f5c66a002b87a4fb133a3e3137b31@194.163.187.175:43656,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,e6e48680fa62c03bed242c52eb21d3cbe44a6752@46.8.210.144:26856,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,1c50df97e155afa50189f48daf41be046c7fe682@85.10.202.135:32656,e0ab3276d94a8fbdf04b0b9eb95df22f7037eb89@167.235.31.186:34656,d71f6a702561b08023810464a96668045dbabd9e@95.214.55.25:26656,50d786a2d242839fe2bdb69bee694d7ffa455824@5.161.60.42:18656,a12f0c225332ab006fbc46d58706669bf44f52e0@113.176.160.117:26656,73e55e512de96e81fa025463f1581daf64172f76@65.108.13.154:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
