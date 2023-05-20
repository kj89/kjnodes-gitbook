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

**live-peers** (21)
```bash
peers="97c4976b580a5ef4c3b82e239c50c81b8ab8189d@49.12.123.87:46656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,0681e865307756c8ac0832d128f00cde11576f37@88.210.13.198:26656,fd5d54740618e8ca6d85cae52ec2db5ea8ac8ea5@91.107.196.77:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,7b9f7827ba8f2698167552d8045c30784a524c19@65.109.89.5:38656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,ba4533a60790009033673e66a53e53fc5db436e4@93.183.208.83:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,7f8bd4eaf6b9b213fd7b89ceefc517bcaa517d24@5.9.147.22:22656,61c3b93bc69ed2b209ffbf959c4a5701e6eb7416@95.217.163.250:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,1b68638343f79c9634ed67923aa8e3ec46c18516@91.142.77.13:26656,d5d51ad6226922fe0a85de41e972722021e6b982@138.201.31.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,a6062857b20b62693523643cb19dc0f3dd4ee961@90.188.249.252:26656,9616c3f4fe9bac03b8b922286207ea66fb7de01f@93.183.208.86:26656,10b77a4ab480c05e323a401b493a08dca2a3ec48@154.53.42.141:26656,0bec869738691df5d0c1f40348c95cd256382f26@89.116.31.114:26656,5b2614774a890a7383e9700e4fc8fa202517ec74@144.91.97.6:26656,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
