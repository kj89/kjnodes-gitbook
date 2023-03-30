# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/althea.png" width="150" alt=""><figcaption></figcaption></figure>

Althea's unique cooperative vision for the internet  brings peering from the data center to the field

**Chain ID**: althea_7357-1 | **Latest Version Tag**: v0.3.2 | **Wasm**: OFF

[Website](https://www.althea.net) | [Discord](https://discord.gg/ZTKWfpDs) | [Twitter](https://twitter.com/altheanetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/althea-testnet](https://explorer.kjnodes.com/althea-testnet)

## Public endpoints

* api: [https://althea-testnet.api.kjnodes.com](https://althea-testnet.api.kjnodes.com)
* rpc: [https://althea-testnet.rpc.kjnodes.com](https://althea-testnet.rpc.kjnodes.com)
* grpc: althea-testnet.grpc.kjnodes.com:52090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@althea-testnet.rpc.kjnodes.com:52656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@althea-testnet.rpc.kjnodes.com:52659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/althea-testnet/addrbook.json > $HOME/.althea/config/addrbook.json
```

**live-peers** (19)
```bash
peers="11e8f38e3c5601e4ab2333d5a5bbb108a39b8e1c@159.69.110.238:26656,ba247bdf826a9636a8276d6a00d8004755f6bb18@162.19.238.210:26656,3f9a20277d68b7fe52efbe84dad231af472d0190@162.55.235.69:29656,ccc09b0fb3c5f6b2dc826a6896bf43b099921bdb@207.180.253.242:26656,5df46d6901ca3487b640950cd0ffedd315536ca1@161.97.139.245:26656,d5040e6aa2f190e04a39dc27e8199786a848e1cd@161.97.99.251:26156,7eb055628aee375914d7d265ef4bc01ea692fe95@65.109.82.106:31656,8af3c5f2e975150cbf2d57bea182c2ca0fb808d2@65.21.237.170:10456,4f3add677b0e4c8dec8b81101ea82620a19d5d0a@65.21.199.148:26633,a3ac64c5c84817f3694a866298399e6ad71ff26c@65.21.53.39:26656,695f6de1a39a5f189015a50ef5f9df144a76b4d8@65.108.233.102:36656,a51b45869b5403dc71251a69879c1eb1c3042bed@65.108.134.215:29336,937dcf8c45b7c64e5188a7036427f2ce86383035@95.165.89.222:24126,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:52656,cd71580f8ab4af6beeaf867702a86ca6f9331f71@65.19.136.133:23296,15e7baf69c0db5c25e26cd1f13eb0d52a7a708b5@142.202.241.235:26656,f6e3f995ba1c3ceed8bd556d9a23d2922d98a9a6@66.172.36.136:14656,d26fddea7ceb8cb5a52223702a23757cb09fad37@207.180.199.115:31656,4f8729168c5454d04ff4a4d7b51986b2e97c68ff@165.232.104.13:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.althea/config/config.toml
```
