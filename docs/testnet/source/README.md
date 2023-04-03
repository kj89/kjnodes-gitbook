# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:28090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (30)
```bash
peers="5f94cf456803179361c44c213fbc95f4da1bc3af@38.242.146.255:26656,7a288e8d085b5aad8d43b0c6e6dbb8498588c206@5.182.17.164:26656,03d324b03078e3bd38c7c7550988362d11106ce4@135.181.198.246:26656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,5755422056c55063f76e4dd0c4245904640ec34b@135.181.149.90:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,b02e2bd359623aeee2d4fad94d37af8b064508f6@167.235.224.141:26656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656,f22864303a45c1f22cdb00f8cfc7f914d18fce9c@135.181.20.30:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,fabc85731f628d8dd1cb20c865c36832ea624772@65.108.88.28:26656,15c65fbabe23372894ba44ee1605276956f8773e@65.109.90.162:26656,2d7b4d18b31b6191e51c2b6641ba6ece814d8aa9@167.235.142.255:26656,7ae84d14c6d12d69b176286dced2746bff483ca8@135.181.178.53:36656,492d7c007dd37f05d2b469865685eb9e4460a379@35.87.85.162:26656,8bf33f58eb977d2a3e8b3159e2949221201044d8@65.109.88.180:26656,cb09ec2e5dc91beaa3d05c79a0a8d6c30fffcc59@65.108.78.101:26656,dd5caa2f3aa0dc1c7491ef21a446363d44b9305c@66.94.125.124:26656,a03f76044c11ae4e6395413745f78ef2a39d5c07@165.232.42.205:26656,4ede26dd5fbb87bd9dba462fe2c3c3e39e15c8f2@207.180.224.128:46656,c0dd01d86ed19becc998874a6a2152513b41f34d@45.84.138.66:28656,9d9c3395668039f7e2109d3be690a97dbb3e9611@194.163.156.184:26656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,0dd9790904c76aee0822dc766468dd67ba5ec0e7@51.81.57.80:10156,46ae715de3bcf284ff997b841e6e82f279e3654f@154.26.153.179:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
