# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (17)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,97c4976b580a5ef4c3b82e239c50c81b8ab8189d@49.12.123.87:46656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,04c7b4c7b1ca40e04e767925c08846d2951f5425@34.23.168.27:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,e2ad22b7cefbddd747c29d90882561e566ff2d3e@65.109.50.106:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,fd5d54740618e8ca6d85cae52ec2db5ea8ac8ea5@91.107.196.77:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
